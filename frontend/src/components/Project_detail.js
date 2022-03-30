import React, {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import {useQuery} from "@apollo/client";
import {GET_PROJECT_DETAIL} from "../query/projects";

const ProjectDetail = ({getProject, item}) =>{
    let {id} = useParams()
    getProject(id)
    // const {data, loading, error} = useQuery(GET_PROJECT_DETAIL, {
    //     variables:{
    //         id: {id}
    //     }
    // })
    // console.log('data=', data)

    return(
        <div>
            <h1>{item.project}</h1>
            <p></p>
            Repository: <a href={item.git_link}>{item.git_link}</a>

        </div>
    )

}

export default ProjectDetail
