import React from "react";
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project_item}) => {
    let link_to_detail = `/project/${project_item.id}`
    return (
        <tr>
            <td>{project_item.id}</td>
            <td>{project_item.project}</td>
            <td>{project_item.git_link}</td>
            <td>{project_item.is_active}</td>
            <td>{project_item.users.id}</td>
            <td><Link to={link_to_detail}>Details</Link></td>
        </tr>
    )
}

const ProjectList = ({project_list}) => {
    return (
        <table>
            <tr>
                <td>id</td>
                <th>Project name</th>
                <th>Link to git</th>
                <th>Active</th>
                <th>Users</th>
                <th>Details</th>
            </tr>
            {project_list.map((project_item) => <ProjectItem project_item={project_item}/>)}
        </table>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
            {item.users.username} ({item.users.email})
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