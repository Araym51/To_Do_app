import React from "react";
import {Table} from "react-bootstrap";
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project_item, deleteProject}) => {
    let link_to_detail = `/project/${project_item.id}`
    return (
        <tr>
            <td>{project_item.id}</td>
            <td>{project_item.project}</td>
            <td>{project_item.git_link}</td>
            <td>{project_item.is_active}</td>
            <td>{project_item.users}</td>
            <td><Link to={link_to_detail}>Details</Link></td>
            <td>
                <button onClick={() => deleteProject(project_item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({project_list, deleteProject}) => {
    return (
        <Link>
            <Link to='projects/create'>New Project</Link>
            <Table striped bordered hover>
                <td>id</td>
                <th>Project name</th>
                <th>Link to git</th>
                <th>Active</th>
                <th>Users</th>
                <th>Details</th>
                {project_list.map((project_item) => <ProjectItem project_item={project_item}
                                                                 deleteProject={deleteProject}/>)}
            </Table>
        </div>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
            {item.username} ({item.email})
        </li>
    )
}

const ProjectDetail = ({getProject, item}) => {
    let {id} = useParams();
    getProject(id)
    let users = item.users ? item.users : []
    console.log('id=', id)
    return (
        <div>
            <h1>{item.project}</h1>
            Repository: <a href={item.git_link}>{item.git_link}</a>
            <p></p>
            Users:
            <ol>
                {users.map((user) => <ProjectUserItem item={user}/>)}
            </ol>
        </div>
    )
}

export {ProjectList, ProjectDetail}