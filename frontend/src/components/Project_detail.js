import React, {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import {useQuery} from "@apollo/client";
import {GET_PROJECT_DETAIL, UPDATE_PROJECT} from "../query/projects";

const ProjectDetail = ({getProject, item}) =>{
    let {id} = useParams()
    getProject(id)
    const {data: items, loading, error} = useQuery(GET_PROJECT_DETAIL, {
        variables:{
            id: `${id}`
        }
    });
    if (loading) return null;
    if (error) return `Error! ${error}`
    console.log('data=', items)

    return(
        <div>
            <h1>{items.projectsId.project}</h1>
            <p></p>
            Repository: <a href={items.projectsId.gitLink}>{items.projectsId.gitLink}</a>
            <p></p>
            Active: {items.projectsId.isActive}
        </div>
    )

}

const UpdateProject = ({getProject}) => {
    let {id} = useParams()
    getProject(id)
    const {data: update, loading: loadingUpdate, error} = useQuery(UPDATE_PROJECT, {
        variables:{
            id:`${id}`
        }
    })
    if (loadingUpdate) return null;
    if (error) return `Error! ${error}`
    console.log('data=', update)
}

export default ProjectDetail
