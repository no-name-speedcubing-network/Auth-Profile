### service responsibilities

root: /user_api/;

#### user
- POST users/ + body - (sign up user) 
- POST users/ + body - (sign in user)
- DELETE users/ + body (delete user)

#### profile
- automatically connect to user_id
- PUT profile/?bio=<murkdown>
- PUT profile/?first_name=<str>
- PUT profile/?last_name=<str>
- PUT profile/?last_name=<str>
- PUT profile/?location=<str>
- PUT profile/?results=<{"3x3": <00:00:00,000>}>
