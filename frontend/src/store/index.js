import { ref, reactive, computed } from "vue"
import { defineStore } from 'pinia'

export const useRoleStore = defineStore('role', () => {

    const role = reactive({
        roleName: '',
        roleID: '',
        roleDesc: '',
        coursesBySkillName: {}
        /*
        coursesBySkillName: {
            skillName1: {
                'skillID': '',
                'courses': {
                    courseName1: {courseDetail1},
                    courseName2: {courseDetail2}
                }
            },
        }
        */
    })

    const storeRole = (roleName, roleID, roleDesc, coursesBySkillName) => {
        role.roleName = roleName
        role.roleID = roleID
        role.roleDesc = roleDesc
        role.coursesBySkillName = coursesBySkillName
    }

    return {
        role,
        storeRole
    }

})

export const useAssignSkillsStore = defineStore('assignSkills', () => {

    const assignSkills = reactive({
        removeSkillsIDArr: [],
        addSkillsIDArr: []
    })

    return {
        assignSkills
    }

})

export const useSkillStore = defineStore('skill', () => {

    const skill = reactive({
        skillName: '',
        skillID: '',
        skillDesc: '',
        coursesBySkillName: {}
        /*
        coursesBySkillName: {
            skillName1: {
                'skillID': '',
                'courses': {
                    courseName1: {courseDetail1},
                    courseName2: {courseDetail2}
                }
            },
        }
        */
    })

    const storeSkill = (skillName, skillID, skillDesc, coursesBySkillName) => {
        skill.skillName = skillName
        skill.skillID = skillID
        skill.skillDesc = skillDesc
        skill.coursesBySkillName = coursesBySkillName
    }

    return {
        skill,
        storeSkill
    }

})
