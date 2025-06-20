from maze import Maze
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        start_cell = m1._Maze__cells[0][0]
        end_cell = m1._Maze__cells[-1][-1]
        
        self.assertFalse(start_cell.has_top_wall)
        self.assertFalse(end_cell.has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 5
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in maze._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()