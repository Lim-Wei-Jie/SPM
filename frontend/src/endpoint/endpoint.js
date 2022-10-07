import axios from "axios";

// Get all Job Roles
export function getAllRoles() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.inventoryList)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all job roles')
            })

    })
}