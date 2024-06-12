SELECT employees.FIRST_NAME
FROM employees
WHERE employee_id IN (
    SELECT DISTINCT manager_id
    FROM employees
);
