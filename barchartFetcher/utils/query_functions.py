import nest_asyncio

nest_asyncio.apply()
import asyncio
from typing import Any, Dict, Optional, Union

import httpx


def sync_query(
    url: str,
    output_format: str = "json",
    headers: Optional[Dict[str, str]] = None,
    cookies: Optional[Dict[str, str]] = None,
    method: str = "GET",
) -> Union[Any, str]:
    """Synchronously fetch an URL.

    Parameters
    ----------
    url : str
        Resource URL.
    output_format : str, default 'json'
        Either 'json' or 'html'.
    headers : dict[str, str] or None, optional
        Extra HTTP headers.
    cookies : dict[str, str] or None, optional
        Cookies to send with the request.

    Returns
    -------
    Any or str
        Parsed JSON (Any) or raw HTML (str).

    Raises
    ------
    ValueError
        If output_format is unsupported.
    httpx.HTTPError
        If the request fails at the transport level.
    Exception
        If the server returns a non-200 status or JSON decoding fails.
    """

    try:
        with httpx.Client(
            headers=headers, cookies=cookies, timeout=30.0
        ) as client:
            client = httpx.Client()

            if method.upper() == "POST":
                response = client.post(url, headers=headers, cookies=cookies)
            else:
                response = client.get(url)

        if response.status_code == 200:
            if output_format == "html":
                return response.text
            if output_format == "json":
                try:
                    return response.json()
                except ValueError as exc:
                    raise Exception(f"Error parsing JSON from {url}") from exc
            raise ValueError(f"Unsupported output format: {output_format}")
        raise Exception(
            f"Error fetching data from {url}: HTTP {response.status_code} - {response.reason_phrase}"
        )
    except httpx.HTTPError as exc:
        raise httpx.HTTPError(
            f"Network error while requesting {url}: {exc}"
        ) from exc


async def async_query(
    async_client: httpx.AsyncClient,
    url: str,
    output_format: str = "json",
    headers: Optional[Dict[str, str]] = None,
    cookies: Optional[Dict[str, str]] = None,
) -> Union[Any, str, Dict[str, str]]:
    """Asynchronously fetch url using async_client.

    Unlike sync_query, no exception is propagated: any failure
    returns {"Error": str} so that async_queries can complete
    even if some requests fail.

    Parameters
    ----------
    async_client : httpx.AsyncClient
        Re-usable asynchronous HTTP client.
    url : str
        Resource URL.
    output_format : str, default 'json'
        Either 'json' or 'html'.
    headers : dict[str, str] or None, optional
        Extra HTTP headers.
    cookies : dict[str, str] or None, optional
        Cookies to send with the request.

    Returns
    -------
    Any or str or dict[str, str]
        Parsed JSON, raw HTML, or {"Error": <msg>} when a failure occurs.
    """

    try:
        response = await async_client.get(
            url,
            headers=headers,
            cookies=cookies,
            timeout=30.0,
        )
    except httpx.HTTPError as exc:
        return {"Error": f"Network error while requesting {url}: {exc}"}

    if response.status_code != 200:
        return {
            "Error": (
                f"Error fetching data from {url}: HTTP {response.status_code} - "
                f"{response.reason_phrase}"
            )
        }

    if output_format == "html":
        return response.text

    if output_format == "json":
        try:
            return response.json()
        except ValueError:
            return {"Error": f"Error parsing JSON from {url}"}

    return {"Error": f"Unsupported output format: {output_format}"}


async def async_queries(
    tasks_dict: Dict[str, Dict[str, str]],
    headers: Optional[Dict[str, str]] = None,
    cookies: Optional[Dict[str, str]] = None,
) -> Dict[str, Union[Any, str, Dict[str, str]]]:
    """Launch multiple asynchronous HTTP GET requests concurrently.

    Each task defined in tasks_dict is executed via async_query.
    Failures for individual requests are captured and surfaced as
    {"Error": <msg>} in the final dictionary, allowing partial success.

    Parameters
    ----------
    tasks_dict : dict[str, dict]
        Mapping key -> {'url': str, 'output_format': str}.
    headers : dict[str, str] or None, optional
        Extra HTTP headers applied to every request.
    cookies : dict[str, str] or None, optional
        Cookies applied to every request.

    Returns
    -------
    dict[str, Union[Any, str, dict[str, str]]]
        Results mapped back to the original tasks_dict keys.
    """

    async with httpx.AsyncClient(headers=headers, cookies=cookies) as client:
        tasks = {
            k: async_query(
                client,
                v["url"],
                v.get("output_format", "json"),
                headers=headers,
                cookies=cookies,
            )
            for k, v in tasks_dict.items()
        }
        results = await asyncio.gather(*tasks.values())
        return {key: result for key, result in zip(tasks.keys(), results)}
