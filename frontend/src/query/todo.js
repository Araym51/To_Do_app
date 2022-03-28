import {gql} from "@apollo/client";

export const GET_ALL_TODO = gql`
query{
        toDo
        {
            id
            project
            {
                project
            }
            noteText
            users
            {
                username
            }
            createdAt
            updatedAt
            isActive
        }
}`