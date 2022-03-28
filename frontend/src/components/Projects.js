import React, {useEffect, useState} from "react";
import {useQuery} from "@apollo/client";
import {GET_ALL_PROJECTS} from "../query/projects";

const ProjectList = () => {
    const {data, loading, error} = useQuery(GET_ALL_PROJECTS)
    const [project, setProjects] = useState([])

    useEffect(() => {
        if (!loading) {
            setProjects(data.projects)
        }
    }, [data])
    if (loading) {
        return <h1>Loading...</h1>
    }

    return (
        <table>
            <th>Project</th>
            <th>Git Link</th>
            <th>Active</th>
            <th>Users</th>
            {project.map(projects =>
            <tr>
                <td>{projects.project}</td>
                <td>{projects.gitLink}</td>
                <td>{projects.isActive}</td>
                <td>{projects.users}</td>
            </tr>
            )}
        </table>)
}

export default ProjectList