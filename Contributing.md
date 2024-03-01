# Contributing

To add a new event, create a pull request modifying the README with the template bellow, filled with your event information:

```md
- [<EVENT-NAME>](<LINK-OR-WEBSITE>)
> Date: <DATE-ISO-FORMAT> || Languages: <COMMA-SEPARATED-VALUES> || Format: <In-Person|Online> || Location: <ADDRESS>
> Description: <OPTIONAL>
```

Using `PyCon US 2024`, it would end up looking like:

```md
- [PyCon US 2024](https://us.pycon.org/2024)
> Date: 2024-05-15 || Languages: English || Format: In-Person, Online || Location: Pittsburgh, Pennsylvalnia
```

---

> NOTE: For the `Date` field, just put the start date for the event.

> NOTE: Don't worry about the order of events; CI would automatically order all entries by date.