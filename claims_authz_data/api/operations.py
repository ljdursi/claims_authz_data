# pylint: disable=invalid-name
# pylint: disable=C0301
"""
Implement endpoints of model service
"""
import uuid
from sqlalchemy import and_
from claims_authz_data import orm
from claims_authz_data.orm import models
from claims_authz_data.api.logging import apilog, logger
from claims_authz_data.api.logging import structured_log as struct_log
from claims_authz_data.api.models import Error, BASEPATH
from claims_authz_data.orm.models import Individual, Consent


def _report_search_failed(typename, exception, **kwargs):
    """
    Generate standard log message + request error for error:
    Internal error performing search

    :param typename: name of type involved
    :param exception: exception thrown by ORM
    :param **kwargs: arbitrary keyword parameters
    :return: Connexion Error() type to return
    """
    report = typename + ' search failed'
    message = 'Internal error searching for '+typename+'s'
    logger().error(struct_log(action=report, exception=str(exception), **kwargs))
    return Error(message=message, code=500)


def _report_update_failed(typename, exception, **kwargs):
    """
    Generate standard log message + request error for error:
    Internal error performing update (PUT)

    :param typename: name of type involved
    :param exception: exception thrown by ORM
    :param **kwargs: arbitrary keyword parameters
    :return: Connexion Error() type to return
    """
    report = typename + ' updated failed'
    message = 'Internal error updating '+typename+'s'
    logger().error(struct_log(action=report, exception=str(exception), **kwargs))
    return Error(message=message, code=500)


@apilog
def get_individuals():
    """
    Return all individuals
    """
    try:
        q = Individual().query.all()
    except orm.ORMException as e:
        err = _report_search_failed('individuals', e, ind_id="all")
        return err, 500

    return [orm.dump(p) for p in q], 200


@apilog
def get_one_individual(individual_id):
    """
    Return single individual object
    """
    try:
        q = Individual().query.get(individual_id)
    except orm.ORMException as e:
        err = _report_search_failed('individual', e, ind_id=str(individual_id))
        return err, 500

    if not q:
        err = Error(message="No individual found: "+str(individual_id), code=404)
        return err, 404

    return orm.dump(q), 200


def individual_exists(db_session, id=None, description=None, **_kwargs):  # pylint:disable=redefined-builtin
    """
    Check to see if individual exists, by ID if given or if by features if not
    """
    if id is not None:
        return db_session.query(models.Individual)\
                          .filter(models.Individual.id == id).count() > 0

    if description is not None:
        return db_session.query(models.Individual)\
                          .filter(models.Individual.description == description).count() > 0

    return False
