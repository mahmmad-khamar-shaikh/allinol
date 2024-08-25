import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AddNoteComponent } from './add-note/add-note.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'Add', component: AddNoteComponent },
];
