import { QuizResponse } from "./QuizResponse";

export interface Question {
  quiz_id: number;
  id: number;
  content: string;
  multipleAnswers: boolean;
  answers: QuizResponse[];
}
