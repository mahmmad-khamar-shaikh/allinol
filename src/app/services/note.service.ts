import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ICard } from '../interface/card';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class NoteService {
  constructor(private http: HttpClient) {}

  getAllNotes(): Observable<ICard[]> {
    return this.http.get<ICard[]>('http://localhost:3000/notes');
  }
}
