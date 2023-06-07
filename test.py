# @pokemon_api.route("", methods=["PUT", "POST"])
# @pokemon_api.route("/<pokemon_id>", methods=["PUT"])
# def update_pokemon(pokemon_id=None):
#     """
#     This API method updates if specified Id (in the endpoint) already exists,
#     else we need to pass the id in the body as JSON format.
#     In the else case, we are using the upsert command to insert and update by changing the method POST/PUT.
#     """
#     if pokemon_id:
#         pokemon = Pokemon.query.get(pokemon_id)

#         if not pokemon:
#             raise NotFoundError("Pokemon not found")

#         # Calling the updated function to update specific attributes
#         update_pokemon_attributes(pokemon, request.json)
#     else:
#         pokemon_data = request.json.get("pokemon")

#         if not pokemon_data:
#             raise NotFoundError("No data provided")

#         # Extract the ID from pokemon_data
#         pokemon_id = pokemon_data.get("id")

#         if not pokemon_id:
#             raise NotFoundError("No ID provided")

#         # Upsert command to insert or update
#         stmt = insert(Pokemon).values(pokemon_data)
#         stmt = stmt.on_conflict_do_update(
#             index_elements=[Pokemon.id],
#             set_={
#                 column.key: stmt.excluded[column.key]
#                 for column in stmt.excluded
#                 if column.key != "id"
#             },
#         )
#         db.session.execute(stmt)
#         db.session.commit()

#     return {
#         "success": True,
#         "message": "Pokemon data updated successfully"
#     }


# def update_pokemon_attributes(pokemon, data):
#     for key, value in data.items():
#         # Skip the ID attribute
#         if key == "id":
#             continue

#         setattr(pokemon, key, value)

#     db.session.add(pokemon)
#     db.session.commit()

iuhf