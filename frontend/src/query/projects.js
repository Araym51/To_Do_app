import {gql} from "@apollo/client";

export const GET_ALL_PROJECTS = gql`
query{
    projects{
        id
        project
        gitLink
        isActive
        users{
            username
            }
        }
    }
`


export const GET_PROJECT_DETAIL = gql`
query projectsId($id: ID){
    projectsId(id: $id){
        id
        project
        gitLink
        isActive
        }
    }
`
