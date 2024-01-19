# Python - Sweet Object-relational Magic 💖🌟

![MONTY GIF](https://media.giphy.com/media/oGAM2NfiX50ac/giphy.gif)

Hey there, fabulous developer! Welcome to this enchanting Python project where we dive into the world of object-relational mapping (ORM) with a touch of girly flair. 💁‍♀️✨

In this whimsical journey, I've mastered the art of connecting with databases using MySQLdb and the elegant SQLAlchemy. Together, we can query, create, edit, and delete tables in the magical realm of MySQL. 🦄🔮

## Tests: ✅💫

* [tests](./tests): A dazzling folder filled with SQL and Python scripts, graciously provided by ALX, to conjure up test tables for all our files.

## Tasks: 📜💖

* **0. Get all states**
  * [0-select_states.py](./0-select_states.py): A spellbinding Python script using MySQLdb to reveal all states in the mystical database `hbtn_0e_0_usa`.
  * Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
  * Results are gracefully ordered by ascending `states.id`.

* **1. Filter states**
  * [1-filter_states.py](./1-filter_states.py): A magical Python script with MySQLdb to unveil all states whose names commence with the letter 'N' in the enchanted database `hbtn_0e_0_usa`.
  * Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.
  * Results are elegantly ordered by ascending `states.id`.

* **2. Filter states by user input**
  * [2-my_filter_states.py](./2-my_filter_states.py): A charming Python script, utilizing MySQLdb, to showcase all values matching a given name in the delightful `states` table of the magical database `hbtn_0e_0_usa`.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
  * Results are arranged in ascending order by `states.id`, crafted with the finesse of string formatting.

* **3. SQL Injection...**
  * [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): An enchanting Python script employing MySQLdb to gracefully display all values matching a given name in the `states` table, ensuring protection against pesky SQL injections.
  * Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.

* **4. Cities by states**
  * [4-cities_by_state.py](./4-cities_by_state.py): A bewitching Python script with MySQLdb, revealing all cities within the mystical database `hbtn_0e_4_usa`.
  * Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.
  * Results are enchantingly ordered by ascending `cities.id`.

* **5. All cities by state**
  * [5-filter_cities.py](./5-filter_cities.py): An adorable Python script using MySQLdb to unveil all cities of a given state in the captivating database `hbtn_0e_4_usa`.
  * Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.
  * Results are sorted with love by ascending `cities.id`.

* **6. First state model**
  * [model_state.py](./model_state.py): A darling Python module introducing a class named `State`, gracefully inheriting from the magical SQLAlchemy `Base`, forming a harmonious connection with the MySQL table `states`.

* **7. All states via SQLAlchemy**
  * [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): A delightful Python script that, with the help of SQLAlchemy, lists all `State` objects from the ethereal database `hbtn_0e_6_usa`.
  * Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`.
  * Results are beautifully sorted by ascending `states.id`.

* **8. First state**
  * [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): A dreamy Python script, enchantingly using SQLAlchemy to print the first `State` object from the magical database `hbtn_0e_6_usa`, gracefully ordered by `states.id`.
  * Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`.
  * If the `states` table is empty, it whispers, "Nothing."

* **9. Contains `a`**
  * [9-model_state_filter_a.py](./9-model_state_filter_a.py): A lovely Python script, using SQLAlchemy to unveil all `State` objects that hold the letter `a` within the charming database `hbtn_0e_6_usa`.
  * Usage: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`.
  * Results are ordered sweetly by ascending `states.id`.

* **10. Get a state**
  * [10-model_state_my_get.py](./10-model_state_my_get.py): A captivating Python script that uses SQLAlchemy to unveil the `id` of the `State` object whose name matches the one passed as an incantation in the mystical database `hbtn_0e_6_usa`.
  * Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.
  * Displays the `id` of the matched `State`.
  * If no match is found, it gently whispers, "Not found."

* **11. Add a new state**
  * [11-model_state_insert.py](./11-model_state_insert.py): A magical Python script using SQLAlchemy to add the `State` object "Louisiana" to the enchanted database `hbtn_0e_6_usa`.
  * Usage: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`.
  * Prints the `id` of the newly created `State` with a touch of sparkle.

* **12. Update a state**
  * [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): A spellbinding Python script, using SQLAlchemy to change the name of the `State` object with `id = 2` in the captivating database `hbtn_0e_6_usa` to the enchanting "New Mexico".
  * Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`.

* **13. Delete states**
  * [13-model_state_delete_a.py](./13-model_state_delete_a.py): A heartwarming Python script using SQLAlchemy to gracefully delete all `State` objects with a name containing the letter `a` from the magical database `hbtn_0e_6_usa`.
  * Usage: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`.

* **14. Cities in state**
  * [model
