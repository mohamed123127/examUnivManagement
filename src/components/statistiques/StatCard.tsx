export function StatCard({ title, value,width }: { title: string; value: string ,width: string}) {
  return (
    <div className={`bg-white rounded-xl shadow-md p-6 border-t-4 border-blue-600 ${width}`}>
      <p className="text-blue-800 font-semibold">{title}</p>
      <p className="text-4xl font-bold text-blue-600 mt-2">{value}</p>
    </div>
  );
}
