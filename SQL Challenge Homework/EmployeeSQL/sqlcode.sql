-- query #1
-- select e.emp_no, e.first_name, e.last_name, e.gender, s.salary 
-- from employees e
-- join salaries s
-- on e.emp_no = s.emp_no
-- ;

-- query #2
-- select e.emp_no, e.first_name, e.last_name 
-- from employees e
-- where date_part('year', hire_date) ='1986'
-- ;

--query #3
-- select d.dept_no, d.dept_name, m.emp_no, e.first_name, e.last_name, m.from_date, m.to_date 
-- from departments d
-- join dept_manager m
-- on d.dept_no = m.dept_no
-- join employees e
-- on m.emp_no = e.emp_no
-- ;

--query #4
-- select e.emp_no, e.first_name, e.last_name, ds.dept_name
-- from employees e
-- join dept_emp d
-- on e.emp_no = d.emp_no
-- join departments ds
-- on d.dept_no =ds.dept_no
-- ;

-- query #5
--List all employees whose first name is "Hercules" and last names begin with "B."
-- select * from employees 
-- where first_name ='Hercules' and last_name like 'B%'
-- ;

-- query #6
--List all employees in the Sales department, including their employee number, 
--last name, first name, and department name.
-- select m.emp_no, e.first_name, e.last_name, d.dept_name
-- from departments d
-- join dept_emp m
-- on d.dept_no = m.dept_no
-- join employees e
-- on m.emp_no = e.emp_no
-- where d.dept_name ='Sales'
-- ;

-- query #7
--List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.
-- select m.emp_no, e.first_name, e.last_name, d.dept_name
-- from departments d
-- join dept_emp m
-- on d.dept_no = m.dept_no
-- join employees e
-- on m.emp_no = e.emp_no
-- where d.dept_name ='Sales' or d.dept_name ='Development'
--;


-- query #8
--In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.

-- select  last_name, count(last_name) as "last name count" from employees
-- group by last_name 
-- order by "last name count" desc
--;





