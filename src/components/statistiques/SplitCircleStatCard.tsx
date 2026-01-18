interface SplitCircleStatCardProps {
  title: string;
  primary: number;   // ex: 51
  secondary: number; // ex: 49
  width: string;
}

export function SplitCircleStatCard({
  title,
  primary,
  secondary,
  width,
}: SplitCircleStatCardProps) {
  const size = 120;
  const stroke = 10;
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;

  const primaryLength = (primary / 100) * circumference;
  const secondaryLength = (secondary / 100) * circumference;

  return (
    <div
      className={`bg-white rounded-xl shadow-md p-6 border-t-4 border-blue-600 ${width}`}
    >
      <div className="flex flex-col items-center">
        <svg width={size} height={size} className="relative">
          {/* Secondary arc */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="#93c5fd" // blue-300
            strokeWidth={stroke}
            fill="none"
            strokeDasharray={`${secondaryLength} ${circumference}`}
            strokeDashoffset={-primaryLength}
          />

          {/* Primary arc */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="#2563eb" // blue-600
            strokeWidth={stroke}
            fill="none"
            strokeDasharray={`${primaryLength} ${circumference}`}
            strokeLinecap="round"
          />

          {/* Primary percentage */}
          <text
            x="50%"
            y="35%"
            textAnchor="middle"
            className="fill-blue-700 text-[10px] font-semibold"
          >
            {primary}%
          </text>

          {/* Secondary percentage */}
          <text
            x="50%"
            y="65%"
            textAnchor="middle"
            className="fill-blue-400 text-[10px] font-semibold"
          >
            {secondary}%
          </text>
        </svg>

        {/* Title at bottom */}
        <p className="mt-3 text-sm font-semibold text-blue-800 text-center">
          {title}
        </p>
      </div>
    </div>
  );
}
