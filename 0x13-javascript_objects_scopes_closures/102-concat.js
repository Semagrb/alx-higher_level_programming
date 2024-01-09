#!/usr/bin/node
const fs = require('fs').promises;

const fArg = process.argv[2];
const sArg = process.argv[3];
const dArg = process.argv[4];

const readFile = async (file) => {
 try {
    const data = await fs.readFile(file, 'utf8');
    return data;
 } catch (err) {
    console.error(err);
 }
};

const writeFile = async (data, file) => {
 try {
    await fs.writeFile(file, data);
 } catch (err) {
    console.error(err);
 }
};

const concatFiles = async () => {
 const fArgData = await readFile(fArg);
 const sArgData = await readFile(sArg);
 const combinedData = fArgData + sArgData;
 await writeFile(combinedData, dArg);
};

concatFiles();
