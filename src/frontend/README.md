# StudySpace Frontend Skeleton

Đây là khung Expo + TypeScript tối giản. Chỉ `App.tsx` có mã để Expo khởi động; các folder feature chưa có code, screen, hook hay API client.

## Chạy ứng dụng

```powershell
npm install
npx expo start
```

## Cấu trúc

```text
App.tsx
src/
├── features/
│   ├── auth/       # gồm profile
│   ├── rooms/      # gồm availability
│   ├── bookings/   # gồm cancellation và notifications
│   └── admin/
└── shared/         # chỉ tạo code dùng chung khi cần
```

Chi tiết screen, hook, API và luồng nghiệp vụ nằm trong `../../SYSTEM_BLUEPRINT.md`. Owner của feature tự tạo file cần thiết khi bắt đầu task.
