# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.v2010.workspace.workflow.statistics import StatisticsContext


class WorkflowList(ListResource):

    def __init__(self, domain, workspace_sid):
        super(WorkflowList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workflows".format(**self._instance_kwargs)

    def read(self, friendly_name=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "FriendlyName": friendly_name,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            WorkflowInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, page_token=None, page=None,
             page_size=None, **kwargs):
        params = values.of({
            "FriendlyName": friendly_name,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            WorkflowInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, configuration, assignment_callback_url,
               fallback_assignment_callback_url=values.unset,
               task_reservation_timeout=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
            "Configuration": configuration,
            "AssignmentCallbackUrl": assignment_callback_url,
            "FallbackAssignmentCallbackUrl": fallback_assignment_callback_url,
            "TaskReservationTimeout": task_reservation_timeout,
        })
        
        return self._domain.create(
            WorkflowInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class WorkflowContext(InstanceContext):

    def __init__(self, domain, workspace_sid, sid):
        super(WorkflowContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workflows/{sid}".format(**self._instance_kwargs)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        return self._domain.fetch(
            WorkflowInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
            "AssignmentCallbackUrl": assignment_callback_url,
            "FallbackAssignmentCallbackUrl": fallback_assignment_callback_url,
            "Configuration": configuration,
            "TaskReservationTimeout": task_reservation_timeout,
        })
        
        return self._domain.update(
            WorkflowInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._domain,
                workspace_sid=self._instance_kwargs['workspace_sid'],
                workflow_sid=self._instance_kwargs['sid'],
            )
        return self._statistics


class WorkflowInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid, sid=None):
        super(WorkflowInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._assignment_callback_url = payload['assignment_callback_url']
        self._configuration = payload['configuration']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._document_content_type = payload['document_content_type']
        self._fallback_assignment_callback_url = payload['fallback_assignment_callback_url']
        self._friendly_name = payload['friendly_name']
        self._sid = payload['sid']
        self._task_reservation_timeout = payload['task_reservation_timeout']
        self._workspace_sid = payload['workspace_sid']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = WorkflowContext(
                self._domain,
                self._context_workspace_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def assignment_callback_url(self):
        """ The assignment_callback_url """
        return self._assignment_callback_url

    @property
    def configuration(self):
        """ The configuration """
        return self._configuration

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def document_content_type(self):
        """ The document_content_type """
        return self._document_content_type

    @property
    def fallback_assignment_callback_url(self):
        """ The fallback_assignment_callback_url """
        return self._fallback_assignment_callback_url

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._friendly_name

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def task_reservation_timeout(self):
        """ The task_reservation_timeout """
        return self._task_reservation_timeout

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._workspace_sid

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            configuration=configuration,
            task_reservation_timeout=task_reservation_timeout,
        )

    def delete(self):
        self._context.delete()