import { reactive, ref } from 'vue'
import { getDailyData } from './backendAPI'


interface DailyData {
    validPokemon: string[][]
    columnCriteria: string[]
    rowCriteria: string[]
}


let templateData: DailyData = {
    validPokemon: [[], [], [], [], [], [], [], [], []],
    columnCriteria: ["", "", ""],
    rowCriteria: ["", "", ""],
}

export const dailyData = await getDailyData() || templateData

export const pokemonNames = reactive(["", "", "", "", "", "", "", "", ""])

export const searchIndex = ref(-1)

export const validPokemon = dailyData.validPokemon

export const rowCriteria = dailyData.rowCriteria

export const columnCriteria = dailyData.columnCriteria

export function isNameLegal(name: string) {
    if (
        name.includes("zygarde-") ||
        name.includes("rockruff-") ||
        name.includes("cramorant-") ||
        name.includes("greninja-") ||
        name.includes("-totem") ||
        (name.includes("pikachu-") && name != "pikachu-gmax") ||
        (name.includes("eevee-") && name != "eevee-gmax")
    ) {
        return false
    }
    return true
}
