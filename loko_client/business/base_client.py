from abc import ABC

from loko_client.utils.requests_utils import URLRequest, AsyncURLRequest


GATEWAY = 'http://localhost:9999/routes/'

class OrchestratorClient(ABC):
    """
        An abstract base orchestrator client
    """

    def __init__(self, gateway=GATEWAY):
        self.u = URLRequest(gateway).orchestrator

class AsyncOrchestratorClient(ABC):
    """
        An abstract base orchestrator client
    """

    def __init__(self, gateway, timeout=None):
        self.u = AsyncURLRequest(gateway, timeout).orchestrator
