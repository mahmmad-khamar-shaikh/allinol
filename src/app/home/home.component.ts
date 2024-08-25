import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatChipsModule } from '@angular/material/chips';
import { ICard } from '../interface/card';
import { NoteService } from '../services/note.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [MatCardModule, MatChipsModule, HttpClientModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
})
export class HomeComponent implements OnInit {
  public cardList: ICard[] = [];
  /**
   *
   */
  constructor(private noteService: NoteService) {}

  ngOnInit(): void {
    this.noteService.getAllNotes().subscribe((data) => {
      console.log(data);
      this.cardList = data;
    });
  }

  remove(id: string) {
    console.log(`Card ${id} is selected for removal`);
    this.cardList = this.cardList.filter((card) => card.id !== id);
  }

  done(id: string) {
    this.cardList = this.cardList.map((card) => {
      let st= card.status;
      return {
        ...card,
        status: card.id===id ? true :st
      };
    });
  }
}
