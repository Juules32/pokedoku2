import axios from "axios";

export async function getDailyData() {
    try {
        const response = await axios.get(`http://${import.meta.env.VITE_BACKEND_HOST}/dailyData`);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        return response.data
    } catch (error) {

    }
}