import { reactive, ref } from 'vue'
import { getDailyData } from './backendAPI'


interface DailyData {
    validPokemon: string[][]
    columnCategories: string[]
    rowCategories: string[]
}


let templateData: DailyData = {
    validPokemon: [[], [], [], [], [], [], [], [], []],
    columnCategories: ["", "", ""],
    rowCategories: ["", "", ""],
}

export const dailyData = await getDailyData() || templateData

export const pokemonNames = reactive(["", "", "", "", "", "", "", "", ""])

export const searchIndex = ref(-1)

export const validPokemon = dailyData.validPokemon

export const rowCategories = dailyData.rowCategories

export const columnCategories = dailyData.columnCategories
