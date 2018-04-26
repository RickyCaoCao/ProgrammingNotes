# General Security Notes

## Passwords

Bad Password:
 - Short passwords (super easy to crack with random guessing), especially when hashes has been exploited)
 - Magic tables (use salting to prevent)
 - A lot of words (each word becomes a letter)

Salting
- Salts are different for every person, every pass
Pepper
- Random data appended to every password

SHA-1, SHA-256
- For quick calculations (e.g. file transferring)
- Instead, we can slow it down by iterating (key stretching)

Adaptive Hashing
- Iteration count can be increased based on hardware capabilities 

Use bcrypt, scrypt, PBKDF2

## SQL Injection
- Basically has access to everything (using union statements)
- Don’t use escaping
- Use parameter validation (but doesn’t always work)
- Use prepared statements (SQL statement template)
    - Constant values are replaced at runtime
    - SELECT * FROM users WHERE username=:name
    - bind(:name, ‘the_string’)
- SQL Injection Links

## Encryption

Encryption Types
	Symmetric/Asymmetric - is key to encrypt and decrypt same or not
	Block Cipher - data encrypted in chunks
	Public/Private Key - You have private key, everyone has public key
	Stream Cipher - data encrypted on the fly (vs. Block cipher)

Perfect Forward Secrecy - can’t go back with a key and decrypt

Encryption at Rest - AES-256, KMS, Full Disk Encryption

## Secret Management
- no secrets hardcoded
- use Vault for storing app secrets
- do not share secrets over insecure channels (e.g. Slack)
- Never log api keys

### Ways to Secure Tokens
1. Save tokens on separate .env file
  - let the code access the variables using env plugins or libraries (eg. .dotenv for node.js)
  - add .env to .gitignore

## Cross-side Scripting
- sanitize input
- encode on output (do not execute output)
- Look into content security policy

Ember: {{{ }}} disables encoding
<br>
Haml: != disables encoding

Synchronizer Token (csrf_token)
- Session token

Never use GET for state changing actions (e.g. delete)

Use X-Frame Options for all logged in sessions to prevent clickjacking

## Information Leaking (Enumeration)
- Determine if certain accounts exist
    - Time between existing and non-existing account to return ‘invalid password’

Gives:
- competitor info
- Know which accounts exist to crack

Solution
- Failure paths should have roughly the same flow
- Avoid true/false requests for account existence

## Session Management
- Session data on server-side (only store references on cookies)
- Verify cookie data
    - Validate expiration
    - Confirm session was created by server
    - Check loose IP (e.g. randomly IP is in Russia)

Session Hijacking - Hacker takes over session of another user
- Ex: stole/guessed session identifier, manipulated badly stored cookie

Session Fixation
- Attacker creates and provides a session ID to a user (thereby, still using same sessions)

Session IDs

- Unique and random
- Cookies should have a domain and `secure` and `httpOnly` flags set
- Regenerate session ID when elevating privileges

<br>
Server Data
- Store session data only on server-side
- Destroy session data on server side too

## Permissions
- Be careful of clipboard copy-paste codes
- Revoke unnecessary priviledges

## Buffer Overflows
- overflowing memory all the way till frame pointer and return address. Then, execute previous code
- Nop Sledding (putting nop codes so that return address goes to a nop and then to executable code)

## Path Traversal
- accessing server files by going off-the-book in URL

## Other Attacks
1. Timing Attack - use timing of operations to infer what's happening
2. Power Analysis - Analyze power consumption of your processor to determine what code is running
3. Acoustic Analysis - analyze sounds (e.g. keyboard clicks)
4. Data remanence - sensitive data that did not actually delete from file system

## Books
- Hacking - The Art of Exploitation -- Jon Erickson