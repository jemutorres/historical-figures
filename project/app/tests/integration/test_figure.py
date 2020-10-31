import json
import pytest
from datetime import date
from requests.models import Response

from starlette.testclient import TestClient


@pytest.mark.usefixtures('test_app_db')
class TestFigure:
    _test_app_db: TestClient
    _figure_name: str
    _figure_description: str
    _figure_birth_date: str
    _figure_death_date: str

    def setup_class(self):
        self._figure_name = 'William Shakespeare'
        self._figure_description = 'English playwright, poet, and actor, widely regarded as the greatest writer ' \
                                   'in the English language and the world\'s greatest dramatist.'
        self._figure_birth_date = '1564-04-26'
        self._figure_death_date = '1616-04-23'

    @pytest.fixture(autouse=True)
    def _request_test_app_db(self, test_app_db):
        self._test_app_db = test_app_db

    def __create_test_figure__(self) -> Response:
        """
        Create a figure and return the response
        :return: response from the server
        :rtype: Response
        """
        return self._test_app_db.post(
            '/figures/',
            data=json.dumps({'name': self._figure_name,
                             'description': self._figure_description,
                             'birth_date': self._figure_birth_date,
                             'death_date': self._figure_death_date})
        )

    def test_create_figure(self) -> None:
        """
        Test to create a figure
        """
        response = self.__create_test_figure__()
        assert response.status_code == 201
        assert response.json()['name'] == self._figure_name
        assert response.json()['description'] == self._figure_description
        assert response.json()['birth_date'] == self._figure_birth_date
        assert response.json()['death_date'] == self._figure_death_date

    def test_create_figure_invalid(self) -> None:
        """
        Test to create a figure with invalid input
        """
        response = self._test_app_db.post(
            '/figures/',
            data=json.dumps(
                {'name': 'dummy', 'description': 'dummy description'})
        )

        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'birth_date'],
                    'msg': 'field required',
                    'type': 'value_error.missing',
                }
            ]
        }

    def test_read_figure(self):
        """
        Test to read a created figure
        """
        figure_id = self.__create_test_figure__().json()['id']
        response = self._test_app_db.get(f'/figures/{figure_id}/')
        assert response.status_code == 200
        assert response.json()['id'] == figure_id

    def test_read_figure_incorrect_id(self):
        """
        Test to get a invalid figure id
        """
        response = self._test_app_db.get('/figures/999/')
        assert response.status_code == 404
        assert response.json()['detail'] == 'Figure not found'

    def test_read_all_figures(self):
        """
        Test to get a figure from all figure list
        """
        figure_id = self.__create_test_figure__().json()['id']
        response = self._test_app_db.get('/figures/')
        assert response.status_code == 200
        assert len(list(filter(lambda d: d['id'] == figure_id, response.json()))) == 1

    def test_update_figure(self):
        """
        Test to update a figure
        """
        figure_id = self.__create_test_figure__().json()['id']
        response = self._test_app_db.put(
            f'/figures/{figure_id}/',
            data=json.dumps(
                {'name': 'The Bard', 'description': '',
                 'birth_date': str(date.today()), 'death_date': self._figure_death_date})
        )
        assert response.status_code == 200
        assert response.json()['name'] == 'The Bard'
        assert response.json()['description'] == ''
        assert response.json()['birth_date'] == str(date.today())
        assert response.json()['death_date'] == self._figure_death_date

    def test_delete_figure(self):
        """
        Test to delete a figure
        """
        figure_id = self.__create_test_figure__().json()['id']
        response = self._test_app_db.delete(f'/figures/{figure_id}/')
        assert response.status_code == 200
        assert response.json()['id'] == figure_id
