export const get = async (url) => {
  const res = await fetch(url);

  if (!res.ok) {
    console.log("El error es", res)
    throw new Error("Failed to fetch data");
  }

  return res.json();
}
