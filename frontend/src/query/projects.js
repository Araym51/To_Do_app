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

export const UPDATE_PROJECT = gql`
            mutation updateProject($id: ID, $gitLink: String!, isActive: $Boolean){
                updateProject(id:$id, gitLink:$gitLink, isActive:$isActive){
                    projects{
                        project
                        id
                        gitLink
                        isActive
                    }
                }
            }`