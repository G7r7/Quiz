import { Question } from "./Question";

export interface Quiz {
  name: string;
  date_creation: Date;
  user_id: number;
  questions: Question[];
}
