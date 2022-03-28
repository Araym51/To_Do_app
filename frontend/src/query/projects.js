import {gql} from "@apollo/client";

export const GET_ALL_PROJECTS = gql`
query{
    projects{
        project
        gitLink
        isActive
        users{
            username
            }
        }
    }
`