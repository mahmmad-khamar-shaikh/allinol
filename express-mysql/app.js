import express from "express";
import { getNote, getNotes, createNote } from "./database.js";
const app = express();
app.use(express.json())
app.get("/notes", async (req, res) => {
  const notes = await getNotes();

  res.send(notes);
});
app.get("/note/:id", async (rq, res) => {
  const id = rq.params.id;

  const notes = await getNote(id);
  res.send(notes);
});
app.post("/notes", async (req, res) => {
    console.log(`body ${req.body}`);
  const { title, content } = req.body;
  const note = await createNote(title, content);
  res.status(201).send(note);
});

app.use((err, req, res, next) => {
  console.log(err.stack);
  res.status(500).send("Something broke");
});

app.listen(3000, () => console.log("listing on port 3000"));
