import json
import pytest
from requests.models import Response

from starlette.testclient import TestClient


@pytest.mark.usefixtures('test_app_db')
class TestQuestion:
    _test_app_db: TestClient
    _question_text: str
    _question_author: str

    def setup_class(self):
        self._question_text = 'What did Shakespeare look like?'
        self._question_author = 'Author'

    @pytest.fixture(autouse=True)
    def _request_test_app_db(self, test_app_db):
        self._test_app_db = test_app_db

    def __create_test_figure__(self) -> int:
        """
        Create a figure and return the response
        :return: figure identifier
        :rtype: int
        """
        response = self._test_app_db.post(
            '/figures/',
            data=json.dumps({'name': 'William Shakespeare',
                             'description': 'English playwright, poet, and actor, widely regarded as the greatest'
                                            ' writer in the English language and the world\'s greatest dramatist.',
                             'birth_date': '1564-04-26',
                             'death_date': '1616-04-23'})
        )
        assert response.status_code == 201
        return response.json()['id']

    def __create_test_question__(self) -> Response:
        """
        Create a question and return the response
        :return: response from the server
        :rtype: Response
        """
        figure_id = self.__create_test_figure__()
        return self._test_app_db.post(
            f'/figures/{figure_id}/questions/',
            data=json.dumps({'question': self._question_text, 'author': self._question_author})
        )

    def test_create_question(self) -> None:
        """
        Test to create a question
        """
        response = self.__create_test_question__()
        assert response.status_code == 201
        assert response.json()['question'] == self._question_text
        assert response.json()['author'] == self._question_author

    def test_create_figure_invalid(self) -> None:
        """
        Test to create a question with invalid input
        """
        figure_id = self.__create_test_figure__()
        response = self._test_app_db.post(
            f'/figures/{figure_id}/questions/',
            data=json.dumps({'author': self._question_author})
        )

        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'question'],
                    'msg': 'field required',
                    'type': 'value_error.missing',
                }
            ]
        }

    def test_read_question(self):
        """
        Test to read a created question
        """
        question = self.__create_test_question__().json()
        question_id, figure_id = question['id'], question['figure_id']
        response = self._test_app_db.get(f'/figures/{figure_id}/questions/{question_id}')
        assert response.status_code == 200
        assert response.json()['id'] == question_id
        assert response.json()['figure_id'] == figure_id

    def test_read_question_incorrect_id(self):
        """
        Test to get a invalid question id
        """
        response = self._test_app_db.get('/figures/999/questions/1/')
        assert response.status_code == 404
        assert response.json()['detail'] == 'Question not found'

    def test_read_all_questions(self):
        """
        Test to get all questions of a figure
        """
        question = self.__create_test_question__().json()
        question_id, figure_id = question['id'], question['figure_id']
        response = self._test_app_db.get(f'/figures/{figure_id}/questions/')
        assert response.status_code == 200
        assert len(list(filter(lambda d: d['id'] == question_id, response.json()))) == 1

    def test_update_figure(self):
        """
        Test to update a question
        """
        question = self.__create_test_question__().json()
        question_id, figure_id = question['id'], question['figure_id']
        response = self._test_app_db.put(
            f'/figures/{figure_id}/questions/{question_id}/',
            data=json.dumps({'question': 'How many plays did Shakespeare write?', 'author': self._question_author})
        )
        assert response.status_code == 200
        assert response.json()['question'] == 'How many plays did Shakespeare write?'
        assert response.json()['author'] == self._question_author

    def test_delete_question(self):
        """
        Test to delete a question
        """
        question = self.__create_test_question__().json()
        question_id, figure_id = question['id'], question['figure_id']
        response = self._test_app_db.delete(f'/figures/{figure_id}/questions/{question_id}/')
        assert response.status_code == 200
