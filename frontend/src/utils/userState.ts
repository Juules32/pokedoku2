import { reactive, ref } from 'vue'
import { getDailyData } from './backendAPI'


interface Criteria {
    category: string
    content: string
}
interface DailyData {
    validPokemon: string[][]
    rowCriteria: Criteria[]
    columnCriteria: Criteria[]
}


let templateData: DailyData = {
    validPokemon: [[], [], [], [], [], [], [], [], []],
    rowCriteria: [
        {
            "category": "",
            "content": ""
        },
        {
            "category": "",
            "content": ""
        },
        {
            "category": "",
            "content": ""
        }
    ],
    columnCriteria: [
        {
            "category": "",
            "content": ""
        },
        {
            "category": "",
            "content": ""
        },
        {
            "category": "",
            "content": ""
        }
    ]
}

export const dailyData = await getDailyData() || templateData

export const pokemonNames = reactive(["", "", "", "", "", "", "", "", ""])

export const searchIndex = ref(-1)

export const validPokemon = dailyData.validPokemon

export const rowCriteria = dailyData.rowCriteria

export const columnCriteria = dailyData.columnCriteria
