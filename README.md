# GraphQL Field Visibility

I found a way to completely hide the fields from users who don't have access rights to them.

To achieve complete field hiding, I used a dynamic schema, that is generated for each user.


| Method | Path         | Action           |
|:------:|--------------|------------------|
| `GET`  | `"/admin"`   | Admin panel      |
| `GET`  | `"/graphql"` | GraphQL Explorer |
