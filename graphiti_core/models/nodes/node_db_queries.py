EPISODIC_NODE_SAVE = """
        MERGE (n:Episodic {uuid: $uuid})
        SET n = {uuid: $uuid, name: $name, group_id: $group_id, source_description: $source_description, source: $source, content: $content, 
        entity_edges: $entity_edges, created_at: $created_at, valid_at: $valid_at}
        RETURN n.uuid AS uuid"""

EPISODIC_NODE_SAVE_BULK = """
    UNWIND $episodes AS episode
    MERGE (n:Episodic {uuid: episode.uuid})
    SET n = {uuid: episode.uuid, name: episode.name, group_id: episode.group_id, source_description: episode.source_description, 
        source: episode.source, content: episode.content, 
    entity_edges: episode.entity_edges, created_at: episode.created_at, valid_at: episode.valid_at}
    RETURN n.uuid AS uuid
"""

ENTITY_NODE_SAVE = """
        MERGE (n:Entity {uuid: $uuid})
        SET n = {uuid: $uuid, name: $name, group_id: $group_id, summary: $summary, created_at: $created_at}
        WITH n CALL db.create.setNodeVectorProperty(n, "name_embedding", $name_embedding)
        RETURN n.uuid AS uuid"""

ENTITY_NODE_SAVE_BULK = """
    UNWIND $nodes AS node
    MERGE (n:Entity {uuid: node.uuid})
    SET n = {uuid: node.uuid, name: node.name, group_id: node.group_id, summary: node.summary, created_at: node.created_at}
    WITH n, node CALL db.create.setNodeVectorProperty(n, "name_embedding", node.name_embedding)
    RETURN n.uuid AS uuid
"""

COMMUNITY_NODE_SAVE = """
        MERGE (n:Community {uuid: $uuid})
        SET n = {uuid: $uuid, name: $name, group_id: $group_id, summary: $summary, created_at: $created_at}
        WITH n CALL db.create.setNodeVectorProperty(n, "name_embedding", $name_embedding)
        RETURN n.uuid AS uuid"""
