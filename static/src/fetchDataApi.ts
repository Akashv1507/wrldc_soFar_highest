import { DataFromApi } from "./index";

export const getSoFarHighestData = async (
  dataSource: string,
  metricName: string
) => {
  try {
    const resp = await fetch(`/api/soFarHighest/${dataSource}/${metricName}`, {
      method: "get",
    });
    const respJSON: DataFromApi = await resp.json();
    return respJSON;
  } catch (e) {
    console.error(e);
    return [];
  }
};