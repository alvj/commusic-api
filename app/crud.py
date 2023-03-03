from sqlmodel import SQLModel, Session


def update_entity(session: Session, current_entity: SQLModel, new_entity: SQLModel) -> SQLModel:
    new_entity_data = new_entity.dict(exclude_unset=True)
    for key, value in new_entity_data.items():
        setattr(current_entity, key, value)

    session.commit()
    session.refresh(current_entity)
    return current_entity
