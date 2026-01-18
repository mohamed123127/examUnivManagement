// export interface Exam {
//   module: KeyValue;
//   classroom: KeyValue;
//   date: Date;
//   time: string;
//   supervisions: KeyValue[];
// }

export interface Exam {
  exam_id: number;
  module_id: number;
  module_name: string;
  date: Date;  // or Date if you parse it
  time: string;
  total_classrooms: number;
  total_profs: number;
}

export type KeyValue = {
  id: number | string;
  value: string;
};