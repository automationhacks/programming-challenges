# System design Interview

## Case study 1: URL shortener

- Build a url shortener like **bit.ly**
- [Source: Interview cake](https://www.interviewcake.com/question/python3/url-shortener?course=fc1&section=system-design)

### Step 1: Decide on what are we building? What features might we need

- Full web app with a web interface?
  - No, API
- If it is an API, do we need user authentication, user accounts, or developer
  keys
  - Make it open to start with
- Can people modify or delete links?
  - Lets leave that out for now
- How long do we retain the links for? Do they persist forever? Or we
  automatically remove old ones
  - Let links live forever
- Should we let people choose their own short-links or just auto generate it? Ex
  `au.ha/ah-resume`
  - Yes
- Do we need analytics? How many people are clicking on the link?
  - Leave it out for now

> Break down into areas like **frontend (web, mobile) or backend, security
> features, User session, data retention, analytics**

### Step 2: Design goals

- If we are designing something, we should know what we are optimizing for.

Some of the design goals can be:

- Should be able to store lot of links, since we are not expiring them.
- As short as possible, having links shorter than the competition can be a
  competitive advantage
- Following a URL should be fast
- API should be resilient to load spikes, one of our links might be the top
  story on reddit

> Can usually break design goals around following properties, **fast, resilient
> to load, data storage**

### Step 3: Building the data model

Think about the database schema, what things do we need to store, how should
they relate to each other, (many to many or one to many relationships), same
table vs different table

- **Take your time naming things, Interviewers find this _quite impressive_
  during an interview**

> ShortLink
>
> - slug
> - destination

### Step 3: Sketching the code

Insights

- Sprint to a naive first draft design so that both interviewer and you can
  optimize
- If there are tricky issues, then you can make a note to come back to these
- Idea is to come up with a skeleton to start building things out from.
- Our default process for answering questions like this is often "make a
  reasonable guess, brainstorm potential issues, and revise"

---

Pseudo code

```text
Below method should be tied to a route like

POST host/api/v1/shortlink
{
    "slug": "ae8uFt",
    "destination": "automationhacks.blog"
}

def generate_short_link(request)
    if request method is not post
        then return a 501 not implemented status code

    if user has provided the slug and it is not existing in the db
        then add a entry in db and return success
    else
        call a generate_random func to generate a unique slug and enter in the
        db

GET host/api/v1/$slug

def redirect(request):
    get destination from db based on slug
    return the original url


def generate_random_slug(request)
    could factor creation time in utc to for uniqueness
```

- Generate random slug can be a tricky issue
  - we would need to figure out how many chars to include
  - what chars to include
  - If we allow `c` different chars for a `n` char long slug then we can have
    `c ^ n` distinct possibilities
  - Figure out the max set of characters we can allow in our random short link
  - Figure out how many distinct possibilities we want to accommodate
  - What chars to allow
    - Should be valid url chars (i.e. `/?#=` etc should not be allowed)
    - Uppercase and lower case char refers to different resources in url, thus
      we can have [A-Z][a-z]
    - Chars should be easy to type on keyboard, we can choose to not allow
      special chars for the sake of readability
    - Special consideration could be to allow either zero (0) or Oh (O) since or
      one (1) vs l(l) since they appear visually similar and we don't know what
      font the user would choose

> Sketching a process like this before jumping in shows methodical thinking. If
> you are not sure how to proceed then write out a process for getting to the
> bottom of things, its fine if you stray from the plan - it'll still help you
> organize your thinking

Tip: Beware of premature optimization! That always looks bad. Don't just jump
around random ideas for optimizations. Instead, focus on asking yourself which
_thing is likely to bottleneck_ first and optimizing around that.

Additional considerations

- What db to use, RDBMS (mySQL, postgres) or NoSQL (mongo, cassandra)
- To speed up we could have data in cache, cache can be invalidated using LRU
  (Least recently used) strategy, If db supports cache natively then it could be
  an advantage, else we could use `memcached`, db sharding can also be an option

As with all system design questions, there are a bunch more directions to go
into with this one. A few ideas:

- At some point we'd probably want to consider splitting our link creation
  endpoint across multiple workers as well. This adds some complexity: how do
  they stay in sync about what the current_random_slug_id is?
- Uptime and "single point of failure" (SPOF) are common concerns in system
  design. Are there any SPOFs in our current architecture? How can we ensure
  that an individual machine failure won't bring down our whole system?
- Analytics. What if we wanted to show users some analytics about the links
  they've created? What analytics could we show, and how would we store and
  display them?
- Editing and deleting. How would we add edit and delete features?
- Optimizing for implementation time. We built something optimized for scale.
  How would our system design be different if we were just trying to get an MVP
  off the ground as quickly as possible?
