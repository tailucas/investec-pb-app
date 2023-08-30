<a name="readme-top"></a>

<!-- ABOUT -->
## About The Project

A simple sample application for the [Python client for Investec Programmable Banking][investec-api-python-url] which performs an integration test against the [Investec Bank API][investec-api-products-url] sandbox endpoint.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SETUP -->
## Setup

Install [Poetry][python-poetry-url] for dependency and runtime management, which already references the client library in the `pyproject.toml` configuration. Follow the instructions on the Poetry site [here][python-poetry-install-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- EXAMPLE -->
## Example Usage

1. Create the credentials file `creds.properties` in the project directory. This is clearly not best practice but good enough to test using the sandbox credentials located in the Investec [API documentation][investec-open-api-docs-url].

```
[creds]
client_id = yAx...5eY
client_secret = 4dY...99r
api_key = eUF4....VBPT0
```

2. From the project directory, run the python application.

```sh
poetry run python app
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIMITATIONS -->
## Limitations

At the time of writing, API sandbox functionality is limited to the [account scope][investec-open-api-docs-url]. The sample application uses a boolean variable `card_sandbox` to skip interactions with the [card scope][investec-open-api-docs-card-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftailucas%2Finvestec-pb-app&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=true)](https://hits.seeyoufarm.com)

[investec-api-python-url]: https://github.com/tailucas/investec-api-python/tree/master
[investec-api-products-url]: https://developer.investec.com/za/api-products
[python-poetry-url]: https://python-poetry.org/
[python-poetry-install-url]: https://python-poetry.org/docs/#installation
[investec-open-api-docs-url]: https://developer.investec.com/za/api-products/documentation/SA_PB_Account_Information
[investec-open-api-docs-card-url]: https://developer.investec.com/za/api-products/documentation/SA_Card_Code
