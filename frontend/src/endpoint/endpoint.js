import axios from "axios";

// Get all Job Roles
export function getAllRoles() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all job roles, check WAMP/MAMP server')
            })
    })
}

// Get specific Job Role details using Job Role ID / Name
export function getRoleDetails(jobRoleName) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/name/${jobRoleName}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0])
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch job role details, check WAMP/MAMP server')
            })
    })
}

// Get all skills assigned to Job Role using Job Role ID
export function getSkillsByRole(jobRoleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/getskill/${jobRoleID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Skill)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills by role, check WAMP/MAMP server')
            })
    })
}

// Get all Courses that fulfils the Skill using Skill ID
export function getCoursesBySkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/getcourse/${skillID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Course)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses by skill, check WAMP/MAMP server')
            })
    })
}

// Create job role
export function createRole(newJobRoleData) {
    var role_id = newJobRoleData[0];
    var role_name = newJobRoleData[1];
    var role_des = newJobRoleData[2];
    // var BE_error = false;
    // var job_err_msg = '';

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/${role_id}/${role_name}/${role_des}`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create role, check WAMP/MAMP server')
            })
    })
}

// Update job role
export function updateRole(roleID, skillIDArr) {
    // const roleID = updateDetails
    console.log(JSON.parse(JSON.stringify(skillIDArr)))
    /*
    Will make 3 concurrent API calls for:
    1. Changes in role name and desc
    2. Addition of skills
    3. Removal of skills
    Can use Promise.all() or Axios.all()
    */
}

// Delete job role
export function deleteRole(roleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/delete/${roleID}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to delete role, check WAMP/MAMP server');
            })
    })
}

// Get all Skills
export function getAllSkills() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.books)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Mapping skills to role
export function mapSkillsToJob(skillstoJobRoleData) {
    var role_id = skillstoJobRoleData[0];
    var skills_id = skillstoJobRoleData[1];

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/roleassignskills/${role_id}/${skills_id}/`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Get specific course using course name
export function getCourseDetails(Course_Name) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/searchcourse/${Course_Name}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Delete skill
export function deleteSkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/delete/${skillID}`
        axios
        .delete(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to delete role, check WAMP/MAMP server');
            })
    })
}

// Get all courses
export function getAllCourses() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/course`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.courses)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
    })
}

// Update skill
export function updateSkill(skillID, skillName, skillDesc) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/update/${skillID}/${skillName}/${skillDesc}`
        axios
        .put(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to update skill details, check WAMP/MAMP server');
            })
    })
}

// add courses to skill
export function addCoursesToSkill(skillID, addCourseIDArr) {
    return new Promise((resolve, reject) => {
        const addedCourses = JSON.parse(JSON.stringify(addCourseIDArr._rawValue))
        //console.log(addCourseIDArr);
        //console.log(addedCourses);
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/${skillID}/${addedCourses}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to add courses to skill, check WAMP/MAMP server');
            })
    })
}

// remove course from skill 
export function removeCoursesFromSkill(skillID, removeCourseIDArr) {
    return new Promise((resolve, reject) => {
        const removedCourses = JSON.parse(JSON.stringify(removeCourseIDArr._rawValue))
        console.log(removeCourseIDArr);
        //console.log(addedCourses);
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/skilldeletecourse/${skillID}/${removedCourses}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to remove course from skill, check WAMP/MAMP server');
            })
    })
}