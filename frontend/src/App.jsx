import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import DashboardLayout from "./layouts/DashboardLayout";

import Login from "./pages/Login";
import Register from "./pages/Register";
import ForgotPassword from "./pages/ForgotPassword";
import ResetPassword from "./pages/ResetPassword";

import Dashboard from "./pages/Dashboard";
import Datasets from "./pages/Datasets";
import Forecast from "./pages/Forecast";
import ForecastWorkspace from "./pages/ForecastWorkspace";
import ScenarioAnalysis from "./pages/ScenarioAnalysis";
import ExecutiveDashboard from "./pages/ExecutiveDashboard";
import AIInsights from "./pages/AIInsights";
import ForecastCollaboration from "./pages/ForecastCollaboration";
import AccuracyCenter from "./pages/AccuracyCenter";
import ExecutiveReports from "./pages/ExecutiveReports";
import Reports from "./pages/Reports";
import Notifications from "./pages/Notifications";
import Users from "./pages/Users";
import Integrations from "./pages/Integrations";
import PermissionManagement from "./pages/PermissionManagement";
import ReportSharing from "./pages/ReportSharing";
import DatasetComparison from "./pages/DatasetComparison";
import DashboardAnalytics from "./pages/DashboardAnalytics";
import ReportScheduling from "./pages/ReportScheduling";
import Profile from "./pages/Profile";
import Settings from "./pages/Settings";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} />

        <Route
          path="/"
          element={
            <ProtectedRoute>
              <DashboardLayout />
            </ProtectedRoute>
          }
        >
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="datasets" element={<Datasets />} />
          <Route path="forecast" element={<Forecast />} />
          <Route path="workspace" element={<ForecastWorkspace />} />
          <Route path="scenarios" element={<ScenarioAnalysis />} />
          <Route path="executive-dashboard" element={<ExecutiveDashboard />} />
          <Route path="ai-insights" element={<AIInsights />} />
          <Route path="collaboration" element={<ForecastCollaboration />} />
          <Route path="accuracy-center" element={<AccuracyCenter />} />
          <Route path="executive-reports" element={<ExecutiveReports />} />
          <Route path="reports" element={<Reports />} />
          <Route path="notifications" element={<Notifications />} />
          <Route path="users" element={<Users />} />
          <Route path="integrations" element={<Integrations />} />
          <Route path="permissions" element={<PermissionManagement />} />
          <Route path="report-sharing" element={<ReportSharing />} />
          <Route path="dataset-comparison" element={<DatasetComparison />} />
          <Route path="dashboard-analytics" element={<DashboardAnalytics />} />
          <Route path="report-scheduling" element={<ReportScheduling />} />
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;