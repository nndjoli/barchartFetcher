from typing import Any, Dict, Union

import nest_asyncio

from barchartFetcher.utils.query_auth_class import QueryAuthClass
from barchartFetcher.utils.query_functions import (
    async_queries as _async_queries,
    sync_query as _sync_query,
)

nest_asyncio.apply()
import asyncio


class QueryManager:

    def __init__(self) -> None:
        """Cache headers and cookies from QueryAuthClass."""
        self._auth = QueryAuthClass()
        self.headers: Dict[str, str] = self._auth.headers
        self.cookies: Dict[str, str] = self._auth.cookies
        self.XSRFToken: str = self._auth.XSRFToken

    def sync_query(
        self, url: str, output_format: str = "json"
    ) -> Union[Any, str]:
        """Fetch a single URL synchronously.

        Parameters
        ----------
        url : str
            Resource URL.
        output_format : str, default "json"
            Either "json" or "html".

        Returns
        -------
        Any or str
            Parsed JSON or raw HTML, depending on *output_format*.

        Examples
        --------
        >>> qm = QueryManager()
        >>> data = qm.sync_query("https://api.example.com/data")
        """
        return _sync_query(
            url,
            output_format=output_format,
            headers=self.headers,
            cookies=self.cookies,
        )

    async def __async_queries(
        self, tasks_dict: Dict[str, Dict[str, str]]
    ) -> Dict[str, Union[Any, str, Dict[str, str]]]:
        """Fetch many URLs concurrently (returns dict)."""
        return await _async_queries(
            tasks_dict,
            headers=self.headers,
            cookies=self.cookies,
        )

    def async_queries(
        self, tasks_dict: Dict[str, Dict[str, str]]
    ) -> Dict[str, Union[Any, str, Dict[str, str]]]:
        """Blocking helper around :py:meth:`async_queries`.

        Parameters
        ----------
        tasks_dict : dict[str, dict]
            Mapping *key -> {"url": str, "output_format": str}*.

        Returns
        -------
        dict[str, Any | str | dict[str, str]]
            Results keyed by *tasks_dict* keys. Failures are surfaced as
            ``{"Error": <message>}``.

        Examples
        --------
        >>> qm = QueryManager()
        >>> tasks = {
        ...     "first": {"url": "https://api.ex1.com", "output_format": "json"},
        ...     "second": {"url": "https://ex2.com/page", "output_format": "html"},
        ... }
        >>> results = qm.run_async_queries(tasks)
        """
        return asyncio.run(self.__async_queries(tasks_dict))
