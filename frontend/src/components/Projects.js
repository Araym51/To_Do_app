import React from "react";
import {Table} from "react-bootstrap";

const ProjectItem = ({project_item}) => {
    return(
        <tr>
            <td>{project_item.project}</td>
            <td>{project_item.git_link}</td>
            <td>{project_item.is_active}</td>
            <td>{project_item.users}</td>
        </tr>
    )
}

const ProjectList = ({project_list}) => {
    return (
        <Table striped bordered hover>
            <th>Project name</th>
            <th>Link to git</th>
            <th>Active</th>
            <th>Users</th>
            {project_list.map((project_item) => <ProjectItem project_item={project_item} />)}
        </Table>
    )
}

export default ProjectList