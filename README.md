# Capital finder

This is a simple serverless function hosted by vercel at <https://capital-finder-khaki.vercel.app/api/capital_finder> using the REST country API (<https://restcountries.com/#rest-countries>) that allows the user to search a country's capital by the name of the country, or to search a country by a capital. It uses the simple `BaseHTTPRequestHandler` function.

Here are example functional links:

* <https://capital-finder-khaki.vercel.app/api/capital_finder?country=France>
  * Search for a capital by the name of the country by appending `?country=[some country]`.
* <https://capital-finder-khaki.vercel.app/api/capital_finder?capital=Lima>
  * Search for a country by capital by appending `?capital=[some capital]`.
* If both arguments are supplied, the search for capital by country name will be prioritized.
